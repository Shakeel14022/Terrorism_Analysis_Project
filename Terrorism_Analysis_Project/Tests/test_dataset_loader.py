import unittest
from scripts.dataset_loader import load_dataset

class TestDatasetLoader(unittest.TestCase):
    def test_load_success(self):
        """Test if the dataset loads successfully and returns a DataFrame."""
        data = load_dataset()
        self.assertIsNotNone(data, "Dataset failed to load.")
        self.assertGreater(data.shape[0], 0, "Dataset has no rows.")
        self.assertGreater(data.shape[1], 0, "Dataset has no columns.")

    def test_file_not_found(self):
        """Test if the function handles missing file correctly."""
        original_file_path = 'Terrorism_Analysis_Project/dataset/globalterrorismdatabase_1970_2020_F.csv'

        # Temporarily change the file path to simulate a missing file
        try:
            import scripts.dataset_loader as loader
            loader.file_path = 'Terrorism_Analysis_Project/dataset/nonexistent_file.csv'
            data = load_dataset()
            self.assertIsNone(data, "Function did not return None for missing file.")
        finally:
            # Restore the original file path after the test
            loader.file_path = original_file_path

    def test_handle_general_exceptions(self):
        """Test if the function handles unexpected exceptions gracefully."""
        try:
            # Simulate an exception by monkey-patching pd.read_csv
            import scripts.dataset_loader as loader
            original_read_csv = loader.pd.read_csv
            loader.pd.read_csv = lambda *args, **kwargs: (_ for _ in ()).throw(Exception("Mock exception"))

            data = load_dataset()
            self.assertIsNone(data, "Function did not return None for a general exception.")
        finally:
            # Restore the original pd.read_csv after the test
            loader.pd.read_csv = original_read_csv

if __name__ == "__main__":
    unittest.main()