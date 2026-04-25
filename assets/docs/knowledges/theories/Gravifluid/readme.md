# Gravifluid

**Gravifluid** (also called "gravefluido" in Portuguese contexts) is a purely geometric effective fluid that arises in certain nonlocal quantum effective actions for gravity, particularly in models that incorporate quantum corrections from Weyl (conformal) anomalies or anomalous gravitational dressings.

The key reference is the 2015 paper *"Quantum Cosmology in Four Dimensions"* by T. Bautista (arXiv:1512.03275), later published in *Classical and Quantum Gravity*.  
In this framework, the authors start from a nonlocal quantum effective action for gravity that includes a cosmological term and quantum corrections. The resulting modified Einstein equations can be rewritten in the standard form:

$$
G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa \left(T_{\mu\nu}^{\text{matter}} + T_{\mu\nu}^{\text{gravifluid}}\right)
$$

where $T_{\mu\nu}^{\text{gravifluid}}$ is the energy‑momentum tensor of the gravifluid. This tensor is of purely geometric origin — it comes from varying the additional nonlocal terms in the effective action with respect to the metric. It can be moved to the left‑hand side (as part of the gravitational sector) or kept on the right as an effective fluid.

## Background: The Nonlocal Effective Action

The model begins with a nonlocal quantum effective action that includes terms sensitive to the conformal (Weyl) anomaly. A simplified form often considered is something like:

$$
S = \int d^4x \sqrt{-g} \left[ \frac{R - 2\Lambda}{2\kappa} + \text{nonlocal quantum corrections involving } \Box^{-1} R \text{ or similar operators} \right]
$$

where $\kappa = 8\pi G$, $R$ is the Ricci scalar, and $\Lambda$ is the bare cosmological constant. The nonlocal operators arise from integrating out quantum fields and lead to anomalous contributions.

Varying this action with respect to the metric yields the modified field equations. In a cosmological setting, these are projected onto a spatially flat Friedmann–Lemaître–Robertson–Walker (FLRW) metric:

$$
ds^2 = -dt^2 + a(t)^2 (dx^2 + dy^2 + dz^2)
$$

with Hubble parameter $H = \dot{a}/a$.

## The Gravifluid in FLRW Cosmology

After applying the equations of motion in this background, the gravifluid’s energy density $\rho$ and pressure $p$ take specific forms involving a parameter $\Gamma$ (related to the strength of the anomalous dressing or the nonlocal kernel) and the cosmological constant $\Lambda$.

From the paper, after using the equations of motion, the gravifluid contributions become proportional to $\Lambda$:

$$
\rho_{\text{gravifluid}} = \frac{\Lambda}{\kappa} \, f(\Gamma, K) \qquad \text{(schematic)}
$$

More precisely, the expressions simplify to forms where:

$$
\rho = \frac{\Lambda}{\kappa} \frac{\Gamma}{1 + \Gamma K} \qquad \text{(or similar combinations, depending on the exact nonlocal kernel)}
$$

and the pressure follows accordingly.

The **equation of state parameter** $w$ for the gravifluid is:

$$
w = \frac{p}{\rho} = -1 + \frac{\Gamma \Lambda}{3 \rho} \qquad \text{(approximate form)}
$$

or more accurately from the derived relations:

$$
w(t) = -1 + \frac{\Gamma \Lambda}{3 \rho(t)}
$$

In the explicit expressions (Eqs. 3.3–3.6 in the paper), the density and pressure of the gravifluid after on‑shell (using equations of motion) are:

$$
\rho_{\text{gravifluid}} \propto \frac{\Lambda \Gamma}{\kappa (1 + \Gamma K)}
$$

$$
p_{\text{gravifluid}} = w \, \rho_{\text{gravifluid}}
$$

with

$$
w = -1 + \frac{\Gamma \Lambda}{3 \rho} \qquad \text{(adjusted for the specific parameterization)}
$$

where $K$ is a parameter related to the nonlocal form factor or the anomalous contribution.

A key point: the gravifluid tensor $T_{\mu\nu}^{K}$ (sometimes denoted with superscript $K$ for the kernel) is **not conserved separately** when there is nonzero interaction or anomalous coupling $\Gamma K \neq 0$. Instead, there is an exchange with the vacuum energy (the bare $\Lambda$ term). The total effective fluid (vacuum + gravifluid) satisfies a modified conservation equation:

$$
\dot{\rho}_{\text{total}} + 3H (\rho_{\text{total}} + p_{\text{total}}) = 0
$$

but individually:

$$
\dot{\rho}_{\text{gravifluid}} + 3H (\rho_{\text{gravifluid}} + p_{\text{gravifluid}}) = -\text{source term involving } \Gamma K
$$

This non‑conservation leads to a slow decay of the vacuum energy, with a slow‑roll parameter proportional to the anomalous gravitational dressings.

## Equation of State Details

In the on‑shell limit for flat FLRW:

- When $\Gamma K = 0$ (no anomalous correction), the gravifluid contribution vanishes or reduces exactly to a cosmological‑constant term ($w = -1$).  
- For nonzero $\Gamma K$, the effective $w$ deviates slightly from $-1$, but remains close to $-1$, producing accelerated expansion.  
- The total momentum tensor becomes proportional to an effective cosmological constant, but modified by quantum corrections. This means:

  - Without bare $\Lambda$, Minkowski space remains an exact solution.  
  - With positive $\Lambda$, the classical de Sitter solution is no longer exact; instead, there is a slow‑roll‑like evolution where the effective vacuum energy decays.

The conservation for the effective fluid reads (schematic):

$$
\dot{\rho}_{\text{eff}} + 3H (\rho_{\text{eff}} + p_{\text{eff}}) = 0
$$

but with $\rho_{\text{eff}} = \rho_{\text{vac}} + \rho_{\text{gravifluid}}$ and a transfer term between them.

## Friedmann Equations with Gravifluid

The modified Friedmann equations become:

$$
3H^2 = \kappa \left(\rho_{\text{matter}} + \rho_{\text{gravifluid}} + \rho_{\Lambda}\right)
$$

$$
2\dot{H} + 3H^2 = -\kappa \left(p_{\text{matter}} + p_{\text{gravifluid}} + p_{\Lambda}\right)
$$

Since $p_{\text{gravifluid}} \approx -\rho_{\text{gravifluid}}$ (with small deviations), the acceleration equation is:

$$
\frac{\ddot{a}}{a} = -\frac{\kappa}{6} (\rho_{\text{total}} + 3p_{\text{total}}) > 0
\qquad
\text{when the effective } w < -1/3
$$

## Physical Interpretation

- **Purely geometric origin**: Unlike ordinary matter or scalar fields, the gravifluid has no microscopic degrees of freedom — it is an emergent description of quantum gravitational corrections.  
- **Role in quantum cosmology**: It provides a mechanism for vacuum energy relaxation or screening without fine‑tuning, potentially addressing aspects of the cosmological constant problem.  
- **Late‑time behavior**: The effective equation of state drives acceleration similar to dark energy, but with possible time dependence due to the nonlocal nature.  
- **Early universe**: In quantum cosmology regimes, these terms can modify the initial singularity or inflation‑like phases.

## Limitations and Extensions

This gravifluid appears specifically in nonlocal effective field theory approaches to quantum gravity (not in full quantum gravity). Different choices of the nonlocal kernel (e.g., exponential form factors or other regulators) change the exact functional form of $\rho$ and $w$.

In related works on Weyl anomalies in cosmology, similar geometric fluids arise, and the gravifluid + vacuum fluid system shows energy exchange when the anomaly coefficient is nonzero.

If you want the **exact equations** from the paper (e.g., the nonlocal action variation, the kernel definition, or the explicit form of $T_{\mu\nu}^{K}$), numerical solutions of the differential equations for $a(t)$, or comparisons with standard $\Lambda$CDM, let me know the precise aspect you'd like to dive deeper into (such as the derivation of $w(t)$ or the structure of the kernel).

Would you like me to set up the differential equations for numerical integration (including code if needed) or focus on the derivation of $w(t)$?
