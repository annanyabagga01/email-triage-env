import random

emails = [

# SPAM
{"email_text":"Win money now!!!","sender":"unknown","subject":"Lottery","task_type":"spam","label":"spam"},
{"email_text":"Limited offer click fast","sender":"unknown","subject":"Offer","task_type":"spam","label":"spam"},
{"email_text":"Meeting tomorrow","sender":"boss","subject":"Meeting","task_type":"spam","label":"not spam"},
{"email_text":"Project update needed","sender":"manager","subject":"Work","task_type":"spam","label":"not spam"},
{"email_text":"Congratulations you won prize","sender":"unknown","subject":"Prize","task_type":"spam","label":"spam"},

# ROUTING
{"email_text":"App crashes","sender":"customer","subject":"Bug","task_type":"routing","department":"Tech"},
{"email_text":"Payment issue","sender":"customer","subject":"Billing","task_type":"routing","department":"Billing"},
{"email_text":"Leave request","sender":"employee","subject":"HR","task_type":"routing","department":"HR"},
{"email_text":"Login problem","sender":"customer","subject":"Login","task_type":"routing","department":"Tech"},
{"email_text":"Invoice missing","sender":"customer","subject":"Invoice","task_type":"routing","department":"Billing"},

# REPLY
{"email_text":"Charged twice","sender":"customer","subject":"Billing","task_type":"reply","ideal_keywords":["sorry","refund"]},
{"email_text":"App not working","sender":"customer","subject":"Bug","task_type":"reply","ideal_keywords":["sorry","fix"]},
{"email_text":"Need help","sender":"customer","subject":"Account","task_type":"reply","ideal_keywords":["help","support"]},
{"email_text":"Refund not received","sender":"customer","subject":"Refund","task_type":"reply","ideal_keywords":["sorry","refund"]},
{"email_text":"Login issue","sender":"customer","subject":"Login","task_type":"reply","ideal_keywords":["sorry","resolve"]}
]

def get_random_email():
    return random.choice(emails)