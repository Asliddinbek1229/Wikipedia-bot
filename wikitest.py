import wikipedia

def sendWikiUz(msg):
    wikipedia.set_lang('uz')

    try:
        res = wikipedia.summary(msg)
        return res
    except:
        return f"😕 {msg} mavzusidagi maqola topilmadi"