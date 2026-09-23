def test_asset_id_type():
    asset_id = "A001"
    assert isinstance(asset_id, str), "Asset ID must be string"
    print("✓ Asset ID is correct type")

def test_cost_type():
    cost = 50000.50
    assert isinstance(cost, float), "Cost must be float"
    print("✓ Cost is correct type")

def test_active_type():
    is_active = True
    assert isinstance(is_active, bool), "Status must be boolean"
    print("✓ Status is correct type")

if __name__ == "__main__":
    test_asset_id_type()
    test_cost_type()
    test_active_type()
    print("\n✓ All variable types validated!")