from pricing import subtotal, discount, shipping


def test_subtotal():
    assert subtotal([(10.0, 2), (5.5, 1)]) == 25.5


def test_discount_known_code():
    assert discount(100, "WELCOME10") == 90.0


def test_discount_unknown_code():
    assert discount(100, "NOPE") == 100


def test_free_shipping_threshold():
    assert shipping(50) == 0.0
    assert shipping(49.99) == 4.90


def test_discount_student():
    assert discount(100, "STUDENT15") == 85.0
