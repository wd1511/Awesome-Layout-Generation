"""Build the selected and detailed READMEs and the standalone catalog pages."""

import re
from pathlib import Path

TITLE = "Awesome Layout Generation"
BADGE = "[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/wd1511/Awesome-Layout-Generation)"
SELECTED = "README.md"
DETAILED = "README-detailed.md"


def read_sections(source):
    _, *parts = re.split(r"^## (.+)\n", source, flags=re.MULTILINE)
    sections = {}
    for heading, body in zip(parts[::2], parts[1::2]):
        body = body.strip()
        if heading.isdecimal() and int(heading) <= 2021:
            slug = "before-2021"
            body = f"### {heading}\n\n{body}"
            legacy_anchor = {"2020": "2019-2020", "2016": "before"}.get(heading)
            if legacy_anchor:
                body = f'<a name="{legacy_anchor}"></a>\n\n{body}'
        else:
            slug = heading.lower()
        sections[slug] = "\n\n".join(filter(None, [sections.get(slug), body]))
    return sections


def label(slug):
    return {"datasets": "Datasets", "before-2021": "2021 and earlier"}.get(slug, slug)


def heading_link(slug):
    return "#" + label(slug).lower().replace(" ", "-")


def render_readme(sections, updated, references, detailed):
    if detailed:
        versions = f"[Selected papers]({SELECTED}) | **Full bibliography**"
        intro = f"The full bibliography of graphic layout generation, poster design, document layouts, and editable graphics. {updated}"
    else:
        versions = f"**Selected papers** | [Full bibliography]({DETAILED})"
        intro = (
            f"Selected papers on graphic layout generation, poster design, document layouts, and editable graphics. {updated} "
            f"For the complete list of papers and their authors, see the [full bibliography]({DETAILED})."
        )
    navigation = " | ".join(f"[{label(slug)}]({heading_link(slug)})" for slug in sections)
    parts = [versions, f"# {TITLE} {BADGE}", intro, navigation]
    if detailed:
        parts.append(
            "**Content-Agnostic** and **Content-Aware** describe how a layout is conditioned. "
            "**LLM-based** identifies the model family and can apply to either setting."
        )
    for slug, body in sections.items():
        resource = "datasets" if slug == "datasets" else "papers"
        if slug == "datasets":
            parts.append('<a name="dataset"></a>')
        parts.extend([f"## {label(slug)}", body, f"[Browse all {resource} →](papers/{slug}.md)"])
    parts.extend(['<a name="reference"></a>', "## References", references])
    parts.append(
        "<details>\n<summary>Updating the bibliography</summary>\n\n"
        "To update the list, edit "
        "[the selection](catalog/selected.md) or [the full catalog](catalog/full.md), "
        "then run `python3 scripts/build_pages.py`.\n\n</details>"
    )
    return "\n\n".join(parts) + "\n"


def render_section(slug, sections, updated):
    section = heading_link(slug)
    short = f"../{SELECTED}{section}"
    full = f"../{DETAILED}{section}"
    title = "Datasets and benchmarks" if slug == "datasets" else f"Papers from {label(slug)}"
    navigation = " | ".join(f"[{label(key)}]({key}.md)" for key in sections)
    parts = [
        f"[Selected papers]({short}) | [Full bibliography]({full})",
        f"# {title}",
        updated,
        navigation,
        sections[slug],
        f"[Back to selected papers]({short}) | [Back to full bibliography]({full})",
    ]
    return "\n\n".join(parts) + "\n"


def build_pages(root):
    catalog_dir = root / "catalog"
    full = (catalog_dir / "full.md").read_text(encoding="utf-8")
    selected = (catalog_dir / "selected.md").read_text(encoding="utf-8")
    full_sections = read_sections(full)
    references = full_sections.pop("references")
    selected_sections = read_sections(selected)
    if full_sections.keys() != selected_sections.keys():
        raise ValueError("Each catalog section needs a corresponding selected section.")
    updated = re.search(r"\*\*Last updated: \d{4}-\d{2}-\d{2}\.\*\*", full).group()
    outputs = {
        root / SELECTED: render_readme(selected_sections, updated, references, detailed=False),
        root / DETAILED: render_readme(full_sections, updated, references, detailed=True),
    }
    papers = root / "papers"
    papers.mkdir(exist_ok=True)
    for slug in full_sections:
        outputs[papers / f"{slug}.md"] = render_section(slug, full_sections, updated)
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    build_pages(Path(__file__).resolve().parents[1])
