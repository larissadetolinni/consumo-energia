def main():
    print("⚡ Calculadora Inteligente de Consumo Elétrico ⚡\n")
    
    nome_aparelho = input("Qual o nome do aparelho? (ex: Geladeira): ")
    
    try:
        potencia_w = float(input(f"Qual a potência da(o) {nome_aparelho} em watts (W)? "))
        horas_dia = float(input("Quantas horas por dia o aparelho fica ligado? "))
    except ValueError:
        print("❌ Erro: Por favor, digite apenas números para potência e horas.")
        return

    dias_no_mes = 30
    consumo_mensal_kwh = (potencia_w * horas_dia * dias_no_mes) / 1000
    
    tarifa = 0.75 # Valor do kWh
    custo_mensal = consumo_mensal_kwh * tarifa

    print("\n--- 📊 Resultado ---")
    print(f"Aparelho: {nome_aparelho}")
    print(f"Consumo estimado: {consumo_mensal_kwh:.2f} kWh/mês")
    print(f"Custo estimado: R$ {custo_mensal:.2f}/mês")
    print("--------------------\n")

if __name__ == "__main__":
    main()