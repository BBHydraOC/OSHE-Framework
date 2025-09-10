#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x3F for a 16 chars and 2 line display
String data = "";
char* dataArray;
String data2 = "";

void setup() {
  Serial.begin(9600);

  lcd.init();
  lcd.clear();         
  lcd.backlight();      // Make sure backlight is on
}

void loop() {
  if (Serial.available() > 0) {
  
    // read the incoming byte:
    data = Serial.readString();
  
    // say what you got:
    Serial.print(data);
    int length = data.length();
    data.remove(length-1);

    lcd.setCursor(0,0);   //Set cursor to character 2 on line 0
    lcd.print(data);
  }
}