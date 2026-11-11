#!/usr/bin/env python3
"""Generate files/Saurabh_Kaushik_CV.pdf from the content already on the site
(_pages/cv.md plus _publications/*.md and _talks/*.md front matter), so the
PDF and the live CV page never drift apart by hand-editing one and not the
other.
"""
import glob
import re
import textwrap

import yaml
from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem,
)

INK = colors.HexColor("#1A1D23")
MUTED = colors.HexColor("#5B6470")
ACCENT = colors.HexColor("#0284C7")

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=22, leading=26, textColor=INK, spaceAfter=4),
    "tagline": ParagraphStyle("tagline", fontName="Helvetica", fontSize=11, leading=14, textColor=MUTED, spaceAfter=4),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=9.5, textColor=MUTED, spaceAfter=14),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5, textColor=ACCENT, spaceBefore=14, spaceAfter=6,
                          borderColor=ACCENT, borderWidth=0, leading=15),
    "entry_head": ParagraphStyle("entry_head", fontName="Helvetica-Bold", fontSize=10, textColor=INK, spaceBefore=6, leading=13),
    "entry_meta": ParagraphStyle("entry_meta", fontName="Helvetica-Oblique", fontSize=9, textColor=MUTED, spaceAfter=2, leading=12),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=13, spaceAfter=2),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=13),
}


def front_matter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def esc(s):
    # Helvetica (WinAnsi) lacks a glyph for U+2010/U+2011; normalize to ASCII hyphen.
    s = s.replace("‐", "-").replace("‑", "-")
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def load_publications():
    skip = {"_publications/2010-10-01-paper-title-number-2.md"}
    pubs = []
    for p in sorted(glob.glob("_publications/*.md")):
        if p in skip:
            continue
        fm = front_matter(p)
        if not fm or not fm.get("venue"):
            # entries without a venue are still-unpublished / special-cased below
            if fm and fm.get("title") == "Glacial-Lake-Bench: A Global Multi-Sensor Benchmark Dataset for Evaluating Deep Learning Models for Glacial Lake Mapping":
                fm["venue"] = "Earth System Science Data (ESSD)"
                fm["date"] = "2026-07-09"
            else:
                continue
        pubs.append(fm)
    pubs.sort(key=lambda d: str(d.get("date", "")), reverse=True)
    return pubs


def load_talks():
    talks = []
    for p in sorted(glob.glob("_talks/*.md")):
        fm = front_matter(p)
        if fm and fm.get("title"):
            talks.append(fm)
    talks.sort(key=lambda d: str(d.get("date", "")), reverse=True)
    return talks


def build():
    doc = SimpleDocTemplate(
        "files/Saurabh_Kaushik_CV.pdf",
        pagesize=LETTER,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        title="Saurabh Kaushik - CV",
        author="Saurabh Kaushik",
    )
    story = []

    story.append(Paragraph("Saurabh Kaushik", styles["name"]))
    story.append(Paragraph("Postdoctoral Research Associate &mdash; Geospatial Data Science, Earth Observation, Foundation Models", styles["tagline"]))
    story.append(Paragraph(
        "Madison, WI &middot; saurabh21.kaushik@gmail.com &middot; sk-2103.github.io &middot; "
        "github.com/Sk-2103 &middot; orcid.org/0000-0002-2791-3729",
        styles["contact"],
    ))

    story.append(Paragraph("Education", styles["h2"]))
    story.append(Paragraph("Ph.D., Earth &amp; Environmental Sciences &mdash; Academy of Scientific and Innovative Research (AcSIR) / CSIR-CSIO, India, with the German Aerospace Center (DLR), Germany (2023)", styles["body"]))
    story.append(Paragraph("Specialization: Remote Sensing, Glaciology, Deep Learning and Image Processing", styles["body"]))
    story.append(Paragraph("M.Sc., Remote Sensing &amp; GIS &mdash; Kumaun University, Nainital, India", styles["body"]))

    story.append(Paragraph("Grants and Awards", styles["h2"]))
    awards = [
        "2026 &mdash; NASA Early Career Investigator Program (ECIP) grant, “Physics-Aware Multimodal Foundation Model for Earth's Evolving Cryosphere” ($300,000, 3 years)",
        "2025 &mdash; Young Scientist Travel Award, Debris Cover Glacier Workshop, ISTA Austria ($1,000)",
        "2024 &mdash; Professional Development/Travel Award, Office of Postdoctoral Affairs, OSU ($700)",
        "2019 &mdash; IASC Early Career Scientist Travel Award, ISMASS Workshop, Reykjavik ($1,500)",
        "2019 &mdash; DAAD Bi-Nationally Supervised Doctoral Degree Fellowship (&euro;24,000)",
        "2019 &mdash; Best Poster Award (3rd), 5th International YES Congress, Berlin",
        "2018 &mdash; INSPIRE Fellowship, DST-India ($13,000)",
    ]
    story.append(ListFlowable([ListItem(Paragraph(a, styles["bullet"]), leftIndent=0) for a in awards],
                               bulletType="bullet", start="•", leftIndent=12))

    story.append(Paragraph("Work Experience", styles["h2"]))
    jobs = [
        ("Postdoctoral Research Associate, Tellman Lab &mdash; University of Wisconsin-Madison", "January 2026 &ndash; Present",
         ["Lead development of FloodDuo, a dual foundation-encoder architecture for generalizable high-resolution flood mapping (ISPRS Journal of Photogrammetry and Remote Sensing)",
          "Flood inundation mapping using CNNs, Vision Transformers, and geo-foundational models",
          "Data fusion of Sentinel-1 and Sentinel-2 via feature-based fusion (Transformer and CNN models)"]),
        ("Postdoctoral Research Associate &mdash; University of Arizona", "June 2024 &ndash; January 2026",
         ["NASA-sponsored flood inundation mapping project",
          "Data fusion of Sentinel-1 and Sentinel-2; large-scale satellite data pipelines (PlanetScope, Sentinel-1/2)"]),
        ("Postdoctoral Researcher &mdash; Byrd Polar and Climate Research Center, Ohio State University", "March 2023 &ndash; May 2024",
         ["Developed the Normalized Difference Depression Index (NDDI) for efficient surface depression mapping",
          "Built Python pipelines to process and visualize Sentinel-2 data and model results; SAR analysis at selected sites"]),
        ("Guest Scientist &mdash; German Remote Sensing Data Center (DLR)", "October 2021 &ndash; March 2023",
         ["Developed GLNet, a deep-learning framework for mapping glacial lakes from multisource remote sensing data"]),
        ("Senior/Junior Research Fellow &mdash; CSIR-Central Scientific Instruments Organisation", "February 2018 &ndash; October 2021",
         ["Developed GLNet for supraglacial debris mapping; generated long-term glacier velocity time series",
          "Glacial Lake Outburst Flood modelling in the Western Himalaya"]),
        ("Project Associate &mdash; Punjab Remote Sensing Center", "September 2016 &ndash; January 2018",
         ["Land use/land cover and wetland mapping; spatial data analysis and field data collection"]),
    ]
    for title, dates, bullets in jobs:
        story.append(Paragraph(title, styles["entry_head"]))
        story.append(Paragraph(dates, styles["entry_meta"]))
        story.append(ListFlowable([ListItem(Paragraph(b, styles["bullet"]), leftIndent=0) for b in bullets],
                                   bulletType="bullet", start="•", leftIndent=12))

    story.append(Paragraph("Skills", styles["h2"]))
    story.append(Paragraph(
        "<b>Programming:</b> Python (proficient); Linux, MATLAB, SQL, Git, Bash scripting", styles["body"]))
    story.append(Paragraph(
        "<b>ML/DL:</b> PyTorch, TensorFlow, CNNs, Vision Transformers, geospatial foundation models, "
        "adapters/fine-tuning, NumPy, pandas, scikit-learn", styles["body"]))
    story.append(Paragraph(
        "<b>Remote sensing/GIS:</b> GDAL, rasterio, QGIS, ArcGIS, ENVI, ERDAS IMAGINE, SNAP, GMTSAR, ISCE2, "
        "COSI-Corr, SAR processing, high-performance computing", styles["body"]))

    story.append(Paragraph("Publications", styles["h2"]))
    for pub in load_publications():
        year = str(pub.get("date", ""))[:4]
        venue = pub.get("venue", "")
        story.append(Paragraph(esc(pub["title"]), styles["entry_head"]))
        meta = f"{venue}" + (f", {year}" if year else "")
        story.append(Paragraph(esc(meta), styles["entry_meta"]))

    story.append(Paragraph("Conference Presentations", styles["h2"]))
    conf_items = [
        "Analysis of Climate Variability and Anticipated Risk of Glacial Lake Outburst in Sikkim Himalaya &mdash; 5th International YES Congress, Berlin, 2019",
        "Linking glacial lake expansion with glacier dynamics: South Lhonak Lake, Sikkim Himalaya &mdash; EGU General Assembly 2020",
        "Automated mapping of Eastern Himalayan glacial lakes using deep learning &mdash; EGU General Assembly 2022",
        "Deep learning framework for automated glacial lake mapping &mdash; ISMASS Workshop, Reykjavík, 2022",
        "Searching for Geological Hydrogen with Multisource Remote Sensing Data and AI &mdash; AGU Fall Meeting 2023",
        "Mapping and Analyzing Geological Hydrogen-related ‘Fairy Circles’ using AI-Driven Remote Sensing &mdash; AGU Fall Meeting 2024",
        "Improving urban flood inundation observations using masked autoencoder-based transformers &mdash; AGU 2024",
        "Combining multisource remote sensing data and CNNs for debris cover mapping &mdash; Debris Cover Glacier Workshop, ISTA, Austria, 2024",
    ]
    story.append(ListFlowable([ListItem(Paragraph(c, styles["bullet"]), leftIndent=0) for c in conf_items],
                               bulletType="bullet", start="•", leftIndent=12))

    story.append(Paragraph("Invited Talks", styles["h2"]))
    for talk in load_talks():
        year = str(talk.get("date", ""))[:4]
        story.append(Paragraph(esc(talk["title"].replace("Talk on ", "")), styles["entry_head"]))
        meta = f"{talk.get('venue', '')}" + (f", {year}" if year else "")
        story.append(Paragraph(esc(meta), styles["entry_meta"]))

    story.append(Paragraph("Teaching", styles["h2"]))
    story.append(Paragraph(
        "Course material contributor, University of Wisconsin-Madison &mdash; "
        "“AI for Sustainability” and “AI for Earth Observation”", styles["body"]))

    doc.build(story)


if __name__ == "__main__":
    build()
