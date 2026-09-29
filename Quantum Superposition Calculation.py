 Quantum Superposition Calculation

import math

 Input amplitudes
alpha = float(input("Enter amplitude of |0>: "))
beta = float(input("Enter amplitude of |1>: "))

 Calculate normalization factor
normalization = math.sqrt(alpha**2 + beta**2)

 Normalize amplitudes
alpha = alpha / normalization
beta = beta / normalization

Calculate probabilities
P0 = alpha**2
P1 = beta**2

 Display results
print("\n--- Quantum Superposition ---")
print("Normalized amplitude of |0> =", round(alpha, 4))
print("Normalized amplitude of |1> =", round(beta, 4))

print("\nSuperposition State:")
print("|ψ> =", round(alpha, 4), "|0> +",
      round(beta, 4), "|1>")

print("\nProbability of |0> =", round(P0 * 100, 2), "%")
print("Probability of |1> =", round(P1 * 100, 2), "%")
print("Total probability =", round((P0 + P1) * 100, 2), "%")
