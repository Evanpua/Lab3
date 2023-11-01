import price_info
import price_info as info

def test_cost_of_fruits():
    fruit="orange"
    quantity=10
    cost=price_info.cost_of_fruits(fruit, quantity)
    assert(cost == 14)

def test_total_cost_shopping():
    total_cost=price_info.total_cost_shopping()
    assert (total_cost == 46.75)