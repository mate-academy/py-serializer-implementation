from car.models import Car
from main import deserialize_car_object, serialize_car_object


def test_flow():
    # 1. Cria uma instância fake do modelo Car
    car_original = Car(
        manufacturer="Tesla",
        model="Model S",
        horse_powers=1020,
        is_broken=False,
        problem_description=None,
    )

    print("--- Testando Serialização ---")
    try:
        json_result = serialize_car_object(car_original)
        print(f"Resultado (bytes): {json_result}")
        # Validação: Deve ser bytes e conter os dados
        assert isinstance(json_result, bytes)
        assert b"Tesla" in json_result
        print("✅ Serialização OK!")
    except Exception as e:
        print(f"❌ Erro na Serialização: {e}")

    print("\n--- Testando Desserialização ---")
    try:
        # Usando o JSON gerado acima para voltar a ser objeto
        car_recovered = deserialize_car_object(json_result)

        # Validações de integridade
        assert isinstance(car_recovered, Car)
        assert car_recovered.manufacturer == "Tesla"
        assert car_recovered.horse_powers == 1020
        assert car_recovered.problem_description is None
        print("✅ Desserialização OK!")
    except Exception as e:
        print(f"❌ Erro na Desserialização: {e}")


if __name__ == "__main__":
    test_flow()
