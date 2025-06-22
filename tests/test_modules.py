from modules.autonomous_agent import AutonomousAgent
from modules.offline_mode import OfflineMode


def test_autonomous_agent():
    agent = AutonomousAgent()
    assert agent.act('I am happy') == 'encourage'


def test_offline_toggle():
    o = OfflineMode()
    o.force(True)
    assert o.active
    o.force(False)
    assert isinstance(o.active, bool)
