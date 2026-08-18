char command[20];
int commandIndex = 0;

void setup()
{
    Serial.begin(115200);
}

void loop()
{
    if (Serial.available())
    {
        char receivedCharacter = Serial.read();

        if (receivedCharacter == '\n')
        {
            command[commandIndex] = '\0';

            if (strcmp(command, "STATUS") == 0)
            {
                Serial.println("OK");
            }
            else if (strcmp(command, "TEMP") == 0)
            {
                Serial.println("24.5");
            }
             else if (strcmp(command, "SELFTEST") == 0)
            {
                Serial.println("SELFTEST_PASSED");
            }

            else
            {
                Serial.println("ERROR: unknown command");
            }

            commandIndex = 0;
        }
        else
        {
            if (commandIndex < sizeof(command) - 1)
            {
                command[commandIndex] = receivedCharacter;

                commandIndex++;
            }
        }
    }
}