# Stakeholder Memo — Market-Making Game (Stage 01)

## Audience (Persona)
**Primary:** Quantitative traders / market-making desk lead at a multi-asset trading firm.  
**Secondary:** Trading researchers and PMs evaluating liquidity and execution costs.  

**Persona snapshot:**  
- **Dana**, MM desk lead, monitors spread competitiveness and inventory risk.  
- Pain points: balancing tight quotes to win flow vs. adverse selection in volatile regimes; understanding how competitor quotes shift equilibrium spreads.

## Context & Problem
We need a simplified, transparent model for two competing market makers who set bid–ask spreads to attract order flow while managing risk. The goal is to formalize payoffs, simulate competitive interactions, and identify equilibrium spreads under varying volatility, order-arrival rates, and execution costs.

## Decision & Useful Answer
- **Decision supported:** How tight should we quote (relative to a competitor) given current market conditions?
- **Answer type:** **Descriptive + Predictive**  
  - *Descriptive:* How changes in volatility and order flow elasticity move equilibrium spreads.  
  - *Predictive:* Simulated equilibrium spreads and expected PnL under specified scenarios.
- **Artifact:** Reproducible Python simulation + visualizations (best responses, equilibria, sensitivity plots).

## Success Metrics
- Clear equilibrium identification (or characterization when multiple equilibria).  
- Sensitivity charts showing how equilibrium spread responds to volatility and order-arrival parameters.  
- Stakeholder-ready summary highlighting risks/assumptions and actionable takeaways.

## Assumptions & Constraints (MVP)
- Rational competitors maximizing expected PnL; symmetric information.  
- Order flow share is a function of relative spreads.  
- Inventory/alpha risk summarized via simple penalty or volatility-scaled term.  
- Simulated data only; no proprietary feeds.  
- Lightweight, reproducible in Python/Jupyter; clean code + README.

## Known Unknowns / Risks
- Real markets exhibit **asymmetric information**, inventory constraints, and multi-venue frictions.  
- Functional forms (demand share, risk penalty) may bias results; we will run robustness checks.  
- Multiple equilibria or non-convergence possible in some parameter regions.

## Deliverables (Stage 01 → later)
- **Now (Stage 01):** Scoping paragraph, README mapping goals → lifecycle → deliverables.  
- **Later (Stages 06–09):**  
  - Notebook with payoff functions, best-response dynamics, equilibrium search.  
  - Sensitivity analyses (volatility, order flow elasticity, costs).  
  - Slide summary with assumptions/risks and decision guidance.

## Stretch (post-MVP)
- Repeated game / adaptive competitors (best-response dynamics, simple RL).  
- Stochastic order flow and funding cost shocks (Monte Carlo).  
- Information asymmetry (adverse selection) and inventory constraints.
