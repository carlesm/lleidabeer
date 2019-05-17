#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

WiFiClient espClient;
PubSubClient client(espClient);

const char *ssid = "fameno-iot";
const char *password = "provaprova";
const char *mqtt_server = "172.16.127.251";




void setup()
{
  Serial.begin(9600);
  Serial.println();
  WiFi.begin(ssid, password);
  Serial.print("Connecting as ");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(WiFi.localIP());
  client.setServer(mqtt_server, 1883);
}

void loop()
{
  delay(500);
  Serial.println("Running!");

  while (!client.connected())
  {
    Serial.println("Connecting mqtt");
    client.connect("ESP000");
    delay(2000);
  }
  Serial.println("Connected to MQTT");
  client.publish("sensor","14");
}
