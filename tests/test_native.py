import dolphin_memory_engine_fork


def test_is_hooked_default():
    assert not dolphin_memory_engine_fork.is_hooked()


def test_hook_unhook():
    dolphin_memory_engine_fork.hook()
    dolphin_memory_engine_fork.un_hook()
    assert not dolphin_memory_engine_fork.is_hooked()
