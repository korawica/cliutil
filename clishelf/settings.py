from textwrap import dedent


class BumpVersionConfig:
    V1: str = dedent(
        r"""[bumpversion]
    current_version = {version}
    commit = True
    tag = False
    parse = ^
        (?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)
        (\.(?P<prekind>a|alpha|b|beta|d|dev|rc)(?P<pre>\d+))?
        (\.(?P<postkind>post)(?P<post>\d+))?
    serialize =
        {{major}}.{{minor}}.{{patch}}.{{prekind}}{{pre}}.{{postkind}}{{post}}
        {{major}}.{{minor}}.{{patch}}.{{prekind}}{{pre}}
        {{major}}.{{minor}}.{{patch}}.{{postkind}}{{post}}
        {{major}}.{{minor}}.{{patch}}
    message = :bookmark: Bump up to version {{current_version}} -> {{new_version}}.

    [bumpversion:part:prekind]
    optional_value = _
    values =
        _
        dev
        a
        b
        rc

    [bumpversion:part:postkind]
    optional_value = _
    values =
        _
        post

    [bumpversion:file:{file}]

    [bumpversion:file:{changelog}]
    search = ## Latest Changes
    replace = ## {{new_version}}
    """
    )

    V1_REGEX: str = (
        r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"
        r"(\.(?P<prekind>a|alpha|b|beta|d|dev|rc)(?P<pre>\d+))?"
        r"(\.(?P<postkind>post)(?P<post>\d+))?"
    )

    V2: str = dedent(
        r"""[bumpversion]
    current_version = {version}
    commit = True
    tag = False
    parse = ^
        (?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)
        (\.(?P<prekind>a|alpha|b|beta|d|dev|rc)(?P<pre>\d+))?
        (\.(?P<postkind>post)(?P<post>\d+))?
    serialize =
        {{major}}.{{minor}}.{{patch}}.{{prekind}}{{pre}}.{{postkind}}{{post}}
        {{major}}.{{minor}}.{{patch}}.{{prekind}}{{pre}}
        {{major}}.{{minor}}.{{patch}}.{{postkind}}{{post}}
        {{major}}.{{minor}}.{{patch}}
    message = :bookmark: Bump up to version {{current_version}} -> {{new_version}}.

    [bumpversion:part:prekind]
    optional_value = _
    values =
        _
        dev
        a
        b
        rc

    [bumpversion:part:postkind]
    optional_value = _
    values =
        _
        post

    [bumpversion:file:{file}]

    [bumpversion:file:{changelog}]
    [bumpversion:file:CHANGELOG.md]
    search = {#}{#} Latest Changes
    replace = {#}{#} Latest Changes

        {#}{#} {{new_version}} - {utcnow:%Y-%m-%d}
    """
    )