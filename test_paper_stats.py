import unittest
from paper_stats import analyze_abstract, parse_keywords


class TestPaperStats(unittest.TestCase):

    def test_abstract_word_count(self):
        result = analyze_abstract("AI improves research. Python helps.")
        self.assertEqual(result["word_count"], 5)

    def test_sentence_count(self):
        result = analyze_abstract("First sentence. Second sentence!")
        self.assertEqual(result["sentence_count"], 2)

    def test_character_count(self):
        result = analyze_abstract("AI research.")
        self.assertEqual(result["character_count"], 12)

    def test_keyword_parsing(self):
        result = parse_keywords(" AI, Python, , Research ")
        self.assertEqual(result, ["AI", "Python", "Research"])

    def test_empty_abstract(self):
        result = analyze_abstract("")
        self.assertEqual(result["word_count"], 0)
        self.assertEqual(result["sentence_count"], 0)


if __name__ == "__main__":
    unittest.main()