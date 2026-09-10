## Recursive Entropy

**Recursive entropy** can be defined as a system in which the uncertainty, complexity, or disorder produced by one state becomes input data for the next state.

Instead of:

$$
S_0 \rightarrow S_1
$$

we have:

$$
S_0 \rightarrow S_1 \rightarrow S_2 \rightarrow S_3 \rightarrow \cdots
$$

where each new state depends on the previous state **and on the entropy generated during the previous transition**.

### 1. Basic equation

Let:

* \(S_n\) = system state at iteration \(n\)
* \(E_n\) = entropy at iteration \(n\)
* \(N_n\) = negentropy/information available to reduce uncertainty
* \(D_n\) = external disturbances
* \(C_n\) = corrective/control information

A conceptual recursive model is:

$$
S_{n+1}=F(S_n,E_n,N_n,D_n,C_n)
$$

and:

$$
E_{n+1}=H(S_{n+1},E_n,D_{n+1})
$$

Thus:

$$
\boxed{E_{n+1}=H(F(S_n,E_n,N_n,D_n,C_n),E_n,D_{n+1})}
$$

The important feature is **feedback**.

---

## 2. Recursive entropy in the Destined Entropy framework

Your previous concept can be extended as:

$$
TE_n = \text{Total Entropy at iteration }n
$$

$$
NT_n = \text{available Negentropy}
$$

$$
DE_n = \text{Destined Entropy}
$$

Then define the next state as:

$$
\boxed{
TE_{n+1}
=
TE_n
+
\Delta E_n
-
NT_n
+
DE_n
}
$$

where \(\Delta E_n\) represents newly introduced uncertainty.

But the distinctive recursive component is:

$$
\boxed{
DE_{n+1}=G(DE_n,TE_n,NT_n,R_n)
}
$$

where \(R_n\) represents the result/error information obtained from iteration \(n\).

So the system doesn't simply **reach a destination**.

It continuously recalculates what the destination should mean based on what it has learned.

---

## 3. Recursive entropy loop

A useful conceptual architecture is:

```text
              ┌──────────────────────┐
              │      INITIAL STATE   │
              └──────────┬───────────┘
                         ↓
                  Measure entropy
                         ↓
                  Calculate uncertainty
                         ↓
                 Generate negentropy
                         ↓
                  Apply correction
                         ↓
                  Produce new state
                         ↓
                Measure new entropy
                         ↓
                 Learn from error
                         │
                         └──────────────┐
                                        ↓
                              NEXT ITERATION
```

Mathematically:

$$
S_0
\rightarrow
E_0
\rightarrow
N_0
\rightarrow
S_1
\rightarrow
E_1
\rightarrow
N_1
\rightarrow
S_2
\rightarrow
E_2
\rightarrow\cdots
$$

This creates an **entropy recursion**.

---

# 4. Entropy does not have to mean only "disorder"

For your framework, a broader definition is more useful:

$$
\boxed{
E = \text{unresolved information required to determine/control a state}
}
$$

Then recursive entropy becomes:

$$
\boxed{
E_{n+1}
=
E_n
+
U_n
+
X_n
-
K_n
}
$$

where:

* \(U_n\) = unknown information discovered
* \(X_n\) = environmental change
* \(K_n\) = useful knowledge/control gained

This produces an interesting property:

**learning can increase entropy before it decreases it.**

For example:

```text
Unknown system
      ↓
Investigation
      ↓
Discover 100 new variables
      ↓
Apparent entropy increases
      ↓
Classify variables
      ↓
Model relationships
      ↓
Predict behavior
      ↓
Effective uncertainty decreases
```

So recursive entropy can represent the **expansion → organization → compression of knowledge**.

---

# 5. Recursive entropy and prediction

Introduce a prediction function:

$$
\hat{S}_{n+1}=P(S_n)
$$

After the actual state appears:

$$
S_{n+1}
$$

the prediction error becomes:

$$
R_n = S_{n+1}-\hat{S}_{n+1}
$$

Then that error becomes input to the next iteration:

$$
P_{n+1}=P_n+\Delta P(R_n)
$$

Therefore:

$$
\boxed{
\text{Prediction}
\rightarrow
\text{Reality}
\rightarrow
\text{Error}
\rightarrow
\text{Learning}
\rightarrow
\text{Improved Prediction}
}
$$

This is the computational heart of recursive entropy.

---

# 6. Recursive entropy → recursive negentropy

You can define:

$$
RN_n = f(E_n,R_n,K_n)
$$

where \(RN_n\) is **recursive negentropy**.

Instead of trying to eliminate all entropy—which is generally impossible in an open physical system—the objective becomes:

$$
\boxed{
\min(E_{n+1}\mid E_n,R_n,K_n)
}
$$

while maximizing useful information:

$$
\boxed{
\max(K_{n+1})
}
$$

This creates an adaptive system:

$$
\boxed{
\text{Entropy}
\rightarrow
\text{Measurement}
\rightarrow
\text{Knowledge}
\rightarrow
\text{Correction}
\rightarrow
\text{New Entropy}
\rightarrow
\text{New Knowledge}
}
$$

---

## 7. Infinite recursive formulation

For an indefinitely continuing system:

$$
S_{n+1}=F(S_n)
$$

and therefore:

$$
S_n=F^n(S_0)
$$

where \(F^n\) means applying the transformation \(F\) repeatedly.

The entropy sequence becomes:

$$
\{E_0,E_1,E_2,E_3,\ldots,E_n,\ldots\}
$$

A theoretical **recursive equilibrium** could occur when:

$$
E_{n+1}\approx E_n
$$

while the system itself continues changing:

$$
S_{n+1}\neq S_n
$$

That distinction is important:

> **A system can continuously transform without continuously accumulating uncontrolled uncertainty.**

In your Destined Entropy terminology, this could become the foundation for **continuous self-correction** rather than a fixed final state.

### Compact definition

$$
\boxed{
\textbf{Recursive Entropy}
=
\text{entropy whose consequences become inputs to the next entropy state}
}
$$

And a stronger version for your framework:

$$
\boxed{
RE_{n+1}
=
F(RE_n,\;E_n,\;N_n,\;R_n,\;D_n)
}
$$

**Recursive entropy therefore turns entropy from a one-time quantity into a continuously evolving information process.**
