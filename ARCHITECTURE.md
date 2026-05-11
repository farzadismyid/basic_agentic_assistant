# Agentic Fashion Color Assistant Architecture

## Overview

This project demonstrates a small agentic AI system for fashion color recommendation.

The system combines:
- visual understanding,
- decision-based routing,
- external fashion knowledge,
- grounded recommendations,
- and critic-based revision loops.

---

# Agent Flow

User Image + Text
        ↓
Visual Agent
        ↓
Decision:
Need captioning?
        ↓
Florence-2 Captioning (optional)
        ↓
Knowledge Agent
        ↓
Decision:
Need external grounding?
        ↓
Fashion Rules Retrieval
        ↓
Critic Agent
        ↓
Decision:
Need revision?
        ↓
Loop / Retry
        ↓
Grounded Response Builder

---

# Agents

## Visual Agent
Responsible for:
- extracting dominant colors,
- evaluating image quality,
- deciding whether captioning is needed.

### Decision Variables
- image_quality
- color_confidence
- needs_caption

---

## Knowledge Agent
Responsible for:
- retrieving fashion rules,
- deciding whether external grounding is required.

### Decision Variables
- request_complexity
- retrieval_confidence
- used_external

---

## Critic Agent
Responsible for:
- evaluating response grounding,
- checking completeness,
- triggering revision loops.

### Decision Variables
- grounding_score
- completeness_score
- needs_revision

---

# Key Concepts

## Agentic Behavior
The system dynamically changes execution flow based on decision variables instead of following one rigid pipeline.

## Grounded Recommendations
Recommendations are tied to external fashion rules to reduce unsupported outputs.

## Critic Loop
Weak outputs trigger another reasoning iteration.