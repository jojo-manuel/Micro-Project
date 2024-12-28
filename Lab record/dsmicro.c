#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the stock structure
typedef struct {
    int id;
    char name[50];
    float buy_price;
    float sell_margin;
    float current_price;
} Stock;

// Function prototypes
void addStock(Stock stocks[], int *count);
void updateCurrentPrice(Stock stocks[], int count);
void displayReadyForSale(Stock stocks[], int count);

int main() {
    int choice;
    int stockCount = 0;
    Stock stocks[100]; // Array to hold up to 100 stocks

    while (1) {
        printf("\nStock Management System\n");
        printf("1. Add Stock\n");
        printf("2. Update Current Price\n");
        printf("3. Display Ready for Sale Stocks\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addStock(stocks, &stockCount);
                break;
            case 2:
                updateCurrentPrice(stocks, stockCount);
                break;
            case 3:
                displayReadyForSale(stocks, stockCount);
                break;
            case 4:
                printf("Exiting...\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}

// Function to add a new stock
void addStock(Stock stocks[], int *count) {
    if (*count >= 100) {
        printf("Stock list is full!\n");
        return;
    }

    Stock newStock;
    printf("Enter Stock ID: ");
    scanf("%d", &newStock.id);
    printf("Enter Stock Name: ");
    scanf("%s", newStock.name);
    printf("Enter Buying Price: ");
    scanf("%f", &newStock.buy_price);
    printf("Enter Selling Margin: ");
    scanf("%f", &newStock.sell_margin);
    newStock.current_price = 0.0; // Default current price

    stocks[*count] = newStock;
    (*count)++;
    printf("Stock added successfully!\n");
}

// Function to update the current price of a stock
void updateCurrentPrice(Stock stocks[], int count) {
    int id;
    float price;
    printf("Enter Stock ID to update current price: ");
    scanf("%d", &id);

    for (int i = 0; i < count; i++) {
        if (stocks[i].id == id) {
            printf("Enter new current price for %s: ", stocks[i].name);
            scanf("%f", &price);
            stocks[i].current_price = price;
            printf("Price updated successfully!\n");
            return;
        }
    }

    printf("Stock with ID %d not found!\n", id);
}

// Function to display stocks ready for sale
void displayReadyForSale(Stock stocks[], int count) {
    int readyCount = 0;

    printf("\nStocks Ready for Sale:\n");
    printf("ID\tName\t\tBuy Price\tSell Margin\tCurrent Price\n");
    printf("------------------------------------------------------------\n");

    for (int i = 0; i < count; i++) {
        if (stocks[i].current_price >= stocks[i].buy_price + stocks[i].sell_margin) {
            printf("%d\t%s\t\t%.2f\t\t%.2f\t\t%.2f\n",
                   stocks[i].id, stocks[i].name, stocks[i].buy_price,
                   stocks[i].sell_margin, stocks[i].current_price);
            readyCount++;
        }
    }

    if (readyCount == 0) {
        printf("No stocks are ready for sale.\n");
    }
}

