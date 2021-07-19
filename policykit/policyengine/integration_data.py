integration_data = {
    "opencollective": {
        "readable_name": "Open Collective",
        "description": "Open Collective enables groups to quickly set up a collective, raise funds, and manage them transparently. Connect to an existing Open Collective collective in order to govern expenses from PolicyKit.",
        "config_instructions": "Create an Open Collective user that has admin privileges on the collective. When logged in as the user, select 'Applications' in the top right menu. Generate a new API key and enter it here. PolicyKit will perform actions on Open Collective on behalf of this user.",
        "webhook_instructions": "Register the webhook URL in Open Collective under the Collective > Settings > Webhooks > Add Another Webhook. Make sure the webhook is registered for the entire collective, not for a user account.",
    },
    "loomio": {
        "readable_name": "Loomio",
        "description": "Loomio makes is easy for groups of all shapes and sizes to collaborate and make decisions across time and space. Connect to a Loomio team in order to perform Loomio polls and discussions from PolicyKit.",
        "config_instructions": "Log into Loomio as an administrator, and navigate to Settings > Integrations > Add Integration > API. Select all API scopes. Enter a name for the integration and save. To find the API key, navigate to 'See API Usage' for the new integration.",
        "webhook_instructions": "Log into Loomio as an administrator, and navigate to Settings > Integrations > Edit Integration > Webhook. Enter the Webhook URL. Select Markdown format and all event types.",
    },
    "slack": {"readable_name": "Slack", "hide_config": True},
    "sourcecred": {
        "readable_name": "SourceCred",
        "description": "SourceCred is a tool for communities to measure and reward value creation. Connect to an existing SourceCred instance in order to use Cred and Grain values in PolicyKit policies.",
    },
    "discourse": {
        "readable_name": "Discourse",
        "description": "Discourse is an open source discussion platform. Use it as a mailing list, discussion forum, long-form chat room, and more. Connect PolicyKit to Discourse to govern actions and perform votes on the Discourse platform.",
    },
    "mailgun": {
        "readable_name": "MailGun",
        "description": "Use the MailGun APIs to send emails from PolicyKit policies.",
    },
    "near": {"readable_name": "NEAR", "description": "Make calls to a NEAR smart contracts from PolicyKit policies."},
}
