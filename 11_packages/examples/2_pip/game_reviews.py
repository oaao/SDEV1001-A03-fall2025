# some times you can rename imports for convenience so that
# you don't have to type as much
import pyexcel as pex

def create_game_reviews_excel_file(reviews, output_filename):
    # saves the data to an excel file
    pex.save_as(array=reviews, dest_file_name=output_filename)

def main():
    GAME_REVIEWS_FILE_NAME = "game_reviews.xlsx"
    # the data we're going to write to the excel file
    GAME_REVIEWS = [
        ["Title", "Platform", "Score"],
        ["Elden Ring", "PC", 95],
        ["Stardew Valley", "Switch", 89],
        ["Cyberpunk 2077", "PS5", 82],
        ["No Man's Sky", "PC", 90],
        ["Gollum", "PS5", 43],
    ]

    create_game_reviews_excel_file(GAME_REVIEWS, GAME_REVIEWS_FILE_NAME)
    print(f"Created {GAME_REVIEWS_FILE_NAME} with game reviews.")


if __name__ == "__main__":
    main()
