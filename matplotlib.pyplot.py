import matplotlib.pyplot as plt

# Dünya, atmosfer ve uzay için yaklaşık basınç değerleri (Pascal cinsinden)
locations = ["Deniz Seviyesi", "Stratosfer", "Uzay (Alçak Dünya Yörüngesi)"]
pressures = [101325, 1000, 0.0000001]

plt.figure(figsize=(7,4))
plt.bar(locations, pressures, color=["blue", "green", "black"])
plt.ylabel("Basınç (Pascal)")
plt.title("Dünya'dan Uzaya Basınç Farkı (Vakıum Kanıtı)")

plt.yscale("log") # Logaritmik ölçek, aradaki farkı açıkça gösterir
plt.show()
