import shlex

def alb(entry):
    try:
        doc = {}
        alb_fields = ['type', 'timestamp', 'elb', 'client:client_port', 'target:target_port', 'request_processing_time',
                      'target_processing_time', 'response_processing_time', 'elb_status_code', 'target_status_code',
                      'received_bytes', 'sent_bytes', 'request', 'user_agent', 'ssl_cipher', 'ssl_protocol',
                      'target_group_arn', 'trace_id', 'domain_name', 'chosen_cert_arn']
        log_values = shlex.split(entry, ' ')
        print(len(log_values)==len(alb_fields))
        for i in range(len(alb_fields)):
            if ':' in alb_fields[i]:
                if ':' in log_values[i]:
                    doc[alb_fields[i].split(':')[0]] = log_values[i].split(':')[0]
                    doc[alb_fields[i].split(':')[1]] = log_values[i].split(':')[1]
                else:
                    doc[alb_fields[i].split(':')[0]] = '-'
                    doc[alb_fields[i].split(':')[1]] = '-'
            else:
                doc[alb_fields[i]] = log_values[i]
        return doc
    except Exception as e:
        print(e,i,log_values,alb_fields[i])
        exit()

def elb(entry):
    try:
        doc = {}
        elb_fields = ['timestamp', 'elb', 'client:client_port', 'backend:target_port', 'request_processing_time',
                      'backend_processing_time', 'response_processing_time', 'elb_status_code', 'backend_status_code',
                      'received_bytes', 'sent_bytes', 'request', 'user_agent', 'ssl_cipher', 'ssl_protocol']
        log_values = list(filter(lambda x: len(x) > 0, shlex.split(entry, ' ')))
        print(len(log_values)==len(elb_fields))
        for i in range(len(elb_fields)):
            if ':' in elb_fields[i]:
                if ':' in log_values[i]:
                    doc[elb_fields[i].split(':')[0]] = log_values[i].split(':')[0]
                    doc[elb_fields[i].split(':')[1]] = log_values[i].split(':')[1]
                else:
                    doc[elb_fields[i].split(':')[0]] = '-'
                    doc[elb_fields[i].split(':')[1]] = '-'
            else:
                doc[elb_fields[i]] = log_values[i]
        return doc
    except Exception as e:
        print(e,i,log_values,elb_fields[i])
        exit()