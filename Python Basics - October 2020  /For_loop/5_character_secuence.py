# позиции в текста -> от 0 до последната, a poslednata e (len(text)-1)
text = input()
for position in range(0, len(text)): #da si obhodim csichki pozicii ot 0 do poslednata
    print(text[position]) #iskame za vsqka edna poziciq da vzimame koq e bukvata na syotvetnata poziciq i da q printirame