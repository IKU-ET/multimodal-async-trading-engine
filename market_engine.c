#include <stdio.h>
#include <stdlib.h>
#include <windows.h> // For Sleep function on Windows

int main() {
    printf("[C Muscle Engine] Hardware data processing node active.\n");
    printf("[C Engine] Running low-latency raw memory updates...\n\n");
    
    // Hardcoded array of live raw price inputs to stream
    double mock_exchange_ticks[] = {150.20, 151.45, 152.10, 149.80, 148.50, 153.25, 154.10, 152.00};
    int total_ticks = sizeof(mock_exchange_ticks) / sizeof(mock_exchange_ticks[0]);
    
    // Loop through the data stream at the hardware tier
    for (int i = 0; i < total_ticks; i++) {
        Sleep(1500); // Wait 1.5 seconds to simulate an incoming network packet
        
        double current_price = mock_exchange_ticks[i];
        printf("[C Hardware Layer] Ingested raw price packet: $%.2f\n", current_price);
        
        // --- STEP 9: PASS TO SHARED STORAGE STORAGE LAYER ---
        // We write the raw number directly into a ultra-fast tracking file
        // Real systems map this straight to RAM pointers (Shared Memory)
        FILE *file_ptr = fopen("live_price_shm.txt", "w");
        if (file_ptr != NULL) {
            fprintf(file_ptr, "%.2f", current_price);
            fclose(file_ptr);
        }
    }
    
    printf("\n[C Muscle Engine] Raw data packet stream complete. Terminating node.\n");
    return 0;
}
