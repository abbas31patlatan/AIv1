from models.gguf_loader import GGUFModel


def test_gguf_initial_state():
    model = GGUFModel('fake.gguf')
    assert not model.ready
