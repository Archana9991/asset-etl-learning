def test_asset_id_not_empty():
    asset_id = "A123"
    assert asset_id != "", "Asset ID cannot be empty"
    print("✓ Test passed!")

def test_asset_cost_positive():
    asset_cost = 50000
    assert asset_cost > 0, "Cost must be positive"
    print("✓ Test passed!")

if __name__ == "__main__":
    test_asset_id_not_empty()
    test_asset_cost_positive()
    print("\nAll tests passed! 🎉")