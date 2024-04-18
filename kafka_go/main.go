package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"

	"github.com/segmentio/kafka-go"
)

var list_brokers = []string{"localhost:9093", "localhost:9094"}

const Topic = "my-topic1"

func produce(brokers []string, topic string, data interface{}) {
	jsonData, err := json.Marshal(data)
	if err != nil {
		log.Fatalf("failed to marshal json: %s", err)
		return
	}

	conn, err := kafka.DialLeader(context.Background(), "tcp", brokers[0], topic, 0)
	if err != nil {
		log.Fatalf("failed to dial leader: %s", err)
	}
	defer conn.Close()

	_, err = conn.WriteMessages(
		kafka.Message{Value: []byte(jsonData)},
	)

	if err != nil {
		log.Fatalf("failed to write messages: %s", err)
	}

	fmt.Printf("Produced message to topic %s: %s\n", topic, string(jsonData))
}

func consumer(brokers []string, topic string, yield chan<- interface{}) {
	r := kafka.NewReader(kafka.ReaderConfig{
		Brokers:   brokers,
		Topic:     topic,
		Partition: 0,
		MinBytes:  10e3, // 10KB
		MaxBytes:  10e6, // 10MB
	})
	defer r.Close()

	for {
		m, err := r.ReadMessage(context.Background())
		if err != nil {
			log.Printf("failed to read message: %s", err)
			continue 
		}
		fmt.Printf("message at offset %d: %s = %s\n", m.Offset, string(m.Key), string(m.Value))

		var data map[string]interface{}
		err = json.Unmarshal(m.Value, &data)
		if err != nil {
			log.Printf("failed to unmarshal json: %s", err)
			log.Printf("offending message: %s", string(m.Value))
			continue 
		}
		yield <- data
	}
}

func main() {

	// Produce messages to the topic
	message := map[string]string{"message": "Hello Kafka!", "name": "Kafka Go"}
	produce(list_brokers, Topic, message)

	// Consume messages from the topic
	yeild := make(chan interface{})
	go consumer(list_brokers, Topic, yeild)
	for {
		data := <-yeild
		fmt.Println(data)
	}
}
