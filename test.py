# from yt_dlp import _Params

# test_opts: _Params = {"postprocessor_args"}


# Source - https://stackoverflow.com/a/75100875
# Posted by sinoroc, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-11, License - CC BY-SA 4.0

import importlib.metadata

version_string_of_foo = importlib.metadata.version('Sdlp')

print(version_string_of_foo)