# Market-Making Game  
**Stage:** Problem Framing & Scoping (Stage 01)  

---

## Problem Statement  
This project investigates how two competing market makers set bid–ask spreads in order to attract order flow while managing risk. The core problem is to model this strategic interaction using a game-theoretic framework, simulate it in Python, and identify equilibrium outcomes under different assumptions about demand, volatility, and execution costs. By doing so, the project aims to provide insight into how liquidity providers adjust spreads in competitive environments and how market conditions influence their expected profitability and risk exposure.  

---

## Stakeholder & User  
The primary stakeholders are **quantitative traders and market-making desks**, who must continuously optimize quoting strategies against competitors in real time. Secondary stakeholders include **trading researchers and portfolio managers**, who are interested in how microstructural competition impacts liquidity, spreads, and execution costs.  

---

## Useful Answer & Decision  
The useful answer is both **descriptive** and **predictive**:  
- **Descriptive:** Clarify how changes in volatility or order arrival rates affect equilibrium spreads.  
- **Predictive:** Generate stakeholder-ready artifacts such as simulations, payoff visualizations, and sensitivity analyses that highlight risks, assumptions, and expected competitor behaviors.  
The main deliverable will be a **simulation artifact** (code + visualizations) that supports decision-making around spread optimization.  

---

## Assumptions & Constraints  
- Market makers act rationally and aim to maximize expected profit.  
- Demand/order flow depends on relative spreads between competitors.  
- Symmetric information in the MVP; information asymmetry possible in extensions.  
- Data availability is simulated (no proprietary market data).  
- Computation is lightweight and reproducible in Python/Jupyter.  

---

## Known Unknowns / Risks  
- True market dynamics may involve asymmetric information, inventory constraints, or non-rational behaviors.  
- Simplified payoff functions may not capture full market microstructure complexity.  
- Sensitivity to parameter choices (volatility, demand elasticity) may lead to unstable equilibria.  

---

## Lifecycle Mapping  

Goal → Stage → Deliverable  

- **Define problem of market-making competition** → Problem Framing & Scoping (Stage 01) → Scoping paragraph + README.md  
- **Set up coding environment & repo** → Tooling Setup (Stage 01) → GitHub repo with /data, /src, /notebooks, /docs  
- **Implement payoff functions & simulations** → Modeling (Stage 06–07) → Jupyter notebook with code + charts  
- **Explore impact of assumptions** → Outliers & Risk Assumptions (Stage 04) → Sensitivity analysis visualizations  
- **Summarize findings for stakeholders** → Results Reporting & Stakeholder Communication (Stage 08–09) → Slide deck / memo with risks, assumptions, and conclusions  

---

## Repo Plan  
- **/data/** → Store input parameter configs, generated results.  
- **/src/** → Core Python scripts (payoff functions, simulation engine).  
- **/notebooks/** → Jupyter notebooks for exploration, visualization, and documentation.  
- **/docs/** → Stakeholder memos, slides, or framing artifacts.  

Cadence: Updates committed after each stage; final repo will include clean code, annotated notebooks, and stakeholder-facing documents.  
