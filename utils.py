from quote import Quote 


def give_qoute():
	responce = Quote().give()
	text_to_send = responce['quoteText']
	if responce['quoteAuthor']:
		text_to_send += '\n---\n' + responce['quoteAuthor']
	return text_to_send

