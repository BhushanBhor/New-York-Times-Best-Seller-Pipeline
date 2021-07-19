# !/bin/bash
def a(**kwargs):
    #if records are updated we should email the recepients with new list
    if records != combined:
        email = EmailOperator(
        task_id='send_email',
        to='bhushan.pop@gmail.com',
        subject='Updated top sellers this week',
        html_content='Please find the Updated List of top sellers',
        dag=dag
        )
        email.execute(context=kwargs)
    else:
        pass