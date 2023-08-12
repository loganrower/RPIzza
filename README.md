# RPIzza
Raspberry Pi pizza ordering system
```mermaid

graph TD
   state1(Sleep Mode <br>LCD is off, and Pi listening for key press) -->|No Key Press| state1
   state1 --> |Press any key to start order| state2(Do you want to start an order? )
   state2 -->|Press * to start order| state3(Display and cycle through order options)
   state2 -->|Press # to cancel| state1
   state3 --> |Press * to cycle| state3
   state3 --> |Input Desired Order Number| state4(Are you sure?)
   state3 --> |Press # to cancel| state5(Do you want to cancel your order)
   state4 --> |Press # to cancel| state5
   state4 --> |Press * to continue to payment/confirmation| state6(Payment/Confirmation)
   state5 --> |Press * to cancel order| state1
   state5 --> |Press # to continue your order| state3
```
