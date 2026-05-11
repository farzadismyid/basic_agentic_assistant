# Agentic Fashion Color Assistant

A small multi-agent AI system for grounded fashion color recommendation.

This project demonstrates:
- agentic AI workflows,
- decision-based routing,
- multimodal reasoning,
- evidence-grounded recommendations,
- and critic-based revision loops.

---

# Features

## Visual Understanding
- dominant color extraction
- image quality estimation
- caption routing decisions

## Captioning
- Florence-2 image caption generation

## Knowledge Grounding
- local fashion rule retrieval
- evidence-aware recommendation generation

## Critic Agent
- evaluates grounding quality
- triggers revision loops

## Orchestration
- coordinates all agents dynamically

---

# Architecture

See:

```bash
ARCHITECTURE.md
```

---

# Example Workflow

1. User uploads clothing image
2. Visual agent analyzes image
3. System decides whether captioning is needed
4. Knowledge agent retrieves matching fashion rules
5. Critic evaluates recommendation quality
6. Response builder generates grounded recommendation

---

# Tech Stack

- Python
- uv
- Pillow
- scikit-learn
- Transformers
- Florence-2
- NumPy

---

# Run

```bash
python -m src.main
```

---

# Project Structure

```text
src/
├── agents/
├── generation/
├── knowledge/
├── utils/
```

---

# Future Improvements

- CLIP embeddings
- vector database retrieval
- FastAPI backend
- Streamlit UI
- explanation faithfulness metrics
- RAG-based grounding
- multi-item outfit compatibility