import boto3

def create_session(profile):
    """Creates a boto session

    Args:
        profile (string): AWS profile name

    Returns:
        [object]: Authenticated Boto3 session
    """
    return boto3.Session(profile_name=profile)


def create_client(session, service):
    """Creates a service client from a boto session

    Args:
        session (object): Authenicated boto3 session
        service (string): service name to create the client for

    Returns:
        [object]: client session for specific aws service (eg. accessanalyzer)
    """
    return session.client(service)






def validate_policies(scps, profile):

    access_analyzer = create_client(create_session(profile), "accessanalyzer")

    for scp in scps:
        scp.validate(access_analyzer)