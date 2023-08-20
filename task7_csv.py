import csv


class PublicationStatistics:
    def open_file(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        return text

    def clean_text(self, text):
        text = self.open_file("publication.txt")
        punc = ",;:-.?!"
        for letter in text:
            if letter in punc:
                text = text.replace(letter, '')
            elif letter in '\n':
                text = text.replace(letter, ' ')
        return text

    def split_text_by_words(self, text):
        words = []
        for word in text.split(' '):
            words.append(word)
        return words

    def counter(self, list_of_addendum):
        content = {}
        for el in list_of_addendum:
            if el != '' and el not in content:
                amount = list_of_addendum.count(el)
                amount_uppercase = list_of_addendum.count(el.upper())
                content[el] = amount
                if amount_uppercase > 0:
                    content[el.upper()] = amount_uppercase
        return content

    def write_csv_word_count(self, content):
        with open('word_count.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter='-')
            for key, value in content.items():
                writer.writerow([key, value])

    def split_text_by_letters(self, text):
        words = self.split_text_by_words(text)
        letters = []
        for word in words:
            for letter in word:
                if letter != ' ':
                    letters.append(letter)
        return letters

    def count_all_letters(self, text):
        for letter in text:
            if letter in ' ':
                text = text.replace(letter, '')
        return len(text)

    def write_csv_letter_count(self, content):
        with open('letter_count.csv', 'w') as csvfile:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            text = self.clean_text(self.open_file('publication.txt'))
            amount_of_letters = self.count_all_letters(text)
            for key, value in content.items():
                if key.lower() == key:
                    count_all = value + content.get(key.upper(), 0)
                    count_uppercase = content.get(key.upper(), 0)
                    percentage = round(count_all / amount_of_letters * 100, 2)
                    writer.writerow({'letter': key, 'count_all': count_all, 'count_uppercase': count_uppercase, 'percentage': percentage})

    def create_csv_files(self):
        text = self.clean_text('publication.txt')
        words_of_text = self.split_text_by_words(text.lower())
        self.write_csv_word_count(self.counter(words_of_text))
        letter_of_text = self.counter(self.split_text_by_letters(text))
        self.write_csv_letter_count(letter_of_text)
        return print("CSV files were recreated successfully!")