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
```

This lets every stamped step carry evidence of its behavior (quantified) and roots (qualified), perfect for self-reflection or agent self-diagnosis.

### 2. Process Tree Support

When enabled (`tree_read=True` or `generate_tree=True`), the checker works with a simple JSON tree that maps the evolution of a version or reasoning process.

**Tree Format (Methodology Overview)**  
A directed acyclic graph (DAG) with:
- **root**: the stamped version/process ID
- **nodes**: individual steps (decompose, gate, annotate, etc.)
  - Quantified metrics (e.g., pruning rate, density)
  - Citations (DOI, file, self-reference)
  - Optional tagged_keywords for semantic chaining
- **synthesis**: final convergence summary (density, iterations, pruning)

**Example (Software-Engineering Discussion Context)**  
From an .srec recap of patch-note refinement:

```json
{
  "root": "v1.1#CS-RefB",
  "nodes": [
    {
      "id": "step1",
      "label": "Initial patch note ingestion",
      "type": "decompose",
      "metrics": {"phrases_extracted": 12, "initial_density": 0.58},
      "citation": "notes/v1.1-patch-discussion.srec",
      "tagged_keywords": ["refactoring", "test-driven", "provenance"],
      "children": ["step2"]
    },
    {
      "id": "step2",
      "label": "Keyword tagging & citation qualification",
      "type": "annotate",
      "metrics": {"tags_applied": 5, "citations_added": 3},
      "citation": "DOI:10.5281/zenodo.16585562 - Spiral Theory (generality constraints)",
      "tagged_keywords": ["provenance", "citation-chain"],
      "children": ["step3"]
    },
    {
      "id": "step3",
      "label": "Semantic map synthesis",
      "type": "synthesis",
      "metrics": {"final_density": 0.87, "convergence_iterations": 3},
      "citation": "Version Checker+ v1.1 (self-reference)",
      "tagged_keywords": ["semantic-map", "traceable-evolution"],
      "reflection": "Chained citations from patch notes → Spiral Theory → self-reference create navigable logic map"
    }
  ],
  "synthesis": {
    "final_density": 0.87,
    "convergence_iterations": 3,
    "overall_pruning": 0.75,
    "summary": "From raw discussion to tagged, cited, traceable process tree. Semantic map built via keyword chaining."
  }
}
```

By following citations and tagged keywords across nodes, you can trace a "map of semantic logic"—a navigable path showing how a process evolved.

Full spec and methodology: https://doi.org/10.5281/zenodo.18916090

## Quick Start

1. Install (or just copy the script—no deps required beyond Python stdlib)
2. Run:
   ```bash
   python version_checker.py --version "v1.1" --dir "notes/" --citation "DOI:10.5281/zenodo.16585562"
   ```
3. Get stamp: `v1.1#CS-RefB` (links to your notes directory)

See `sample_notes.yaml` and `process_tree_example.json` for templates.

## Why this tool?

Most version systems are silent. This one speaks—quietly, traceably, and on your terms.  
Whether you're documenting personal projects, open research, or agent workflows, it bridges code to context without complexity.

## License

MIT License – free to use, modify, fork, and build upon.

## Related

- Zenodo: https://doi.org/10.5281/zenodo.18916090
- Spiral Theory: https://doi.org/10.5281/zenodo.16585562
- A.I.S. Standard: https://doi.org/10.5281/zenodo.15176494

Let's keep the spirals turning.
