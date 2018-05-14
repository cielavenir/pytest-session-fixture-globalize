# need to use runpytest_subprocess due to global variable in test resource

pytest_plugins = "pytester"
import pytest

@pytest.mark.parametrize(('options','status','ret'),[
    (['--session-fixture-globalize'],'*2 passed*',0),
    ([],'*1 failed, 1 passed*',1),
])
def test_SessionFixtureGlobalizeNormal(testdir,options,status,ret):
    init = testdir.makepyfile(__init__="""
        import pytest
        cnt=0
        @pytest.fixture(scope="session")
        def val(request):
            global cnt
            cnt+=1
            yield cnt
    """)
    a = testdir.makepyfile(a="""
        from . import val
        def test_a(val):
            assert val==1
    """)
    b = testdir.makepyfile(b="""
        from . import val
        def test_b(val):
            assert val==1
    """)
    result = testdir.runpytest_subprocess(*[init,a,b]+options)
    result.stdout.fnmatch_lines(status)
    assert result.ret ==ret

@pytest.mark.parametrize(('options','status','ret'),[
    (['--session-fixture-globalize'],'*2 passed*',0),
    ([],'*1 passed, 1 error*',1),
])
def test_SessionFixtureGlobalizeAutouse(testdir,options,status,ret):
    init = testdir.makepyfile(__init__="""
        import pytest
        cnt=0
        @pytest.fixture(scope="session",autouse=True)
        def val(request):
            global cnt
            cnt+=1
            assert cnt==1
            yield cnt
    """)
    a = testdir.makepyfile(a="""
        from . import val
        def test_a():
            pass
    """)
    b = testdir.makepyfile(b="""
        from . import val
        def test_b():
            pass
    """)
    result = testdir.runpytest_subprocess(*[init,a,b]+options)
    result.stdout.fnmatch_lines(status)
    assert result.ret ==ret
