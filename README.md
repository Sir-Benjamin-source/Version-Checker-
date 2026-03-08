# Version Checker+

**A lightweight tool to turn version numbers into self-referencing hyperlinks with provenance stamps**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18916090.svg)](https://doi.org/10.5281/zenodo.18916090)

## What it does

Version Checker+ generates a unique stamp (e.g., `v1.2.3#CS-RefA`) that links your version number directly to a directory of your choosing (YAML, text, JSON) containing patch notes, citations, contributors, or process history.  

It's designed for:
- Self-documenting code evolution
- Easy traceability without external services
- Personal or scholarly citation (family lore, Spiral Theory, DOIs, etc.)
- Future AI/agent workflows needing provenance and context

No validation, no tracking—just a simple stamp + your own notes.

## v1.1 – AI-Tailored Provenance & Process Tree Extension (March 2026)

This release adds two extensions to make the tool more useful for iterative reasoning, agent maintenance, and open research:

### 1. Quantified & Citation-Qualified Stamps

Add numerical metrics and traceable citations directly to stamps:

```python
version_check(
    stamp_type='process',
    item='daer_gate',
    quantified_metrics={'pruning_rate': 0.91, 'density_lift': 0.85, 'iterations': 4},
    citation_doi='10.5281/zenodo.16585562'
)
Feedback and contributions are welcome! Open issues or submit pull requests on GitHub. Contact @SirBenjamino0 or xAI support for inquiries.

### Acknowledgments
Thanks to the xAI team for Grok 3’s collaboration, Francis Bacon for empirical inspiration, and the Zenodo community for open-access support.
