from dmock.generators.uri.generator import PureRandomUri, UriGenerator


def test_uri_generator():
    strategy = PureRandomUri()
    generator = UriGenerator(strategy)

    print(generator())
