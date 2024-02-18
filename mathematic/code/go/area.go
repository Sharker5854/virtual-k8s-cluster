package main

import (
	"math"
	"strconv"
	"net/http"
)

func CircleAreaHandler(w http.ResponseWriter, r *http.Request) {
	radius, err := strconv.Atoi(r.FormValue("radius"))
	if err != nil {
		http.Error(w, "Invalid radius parameter", http.StatusBadRequest)
		return
	}
	area := calculateArea(radius)
	w.Write([]byte("Golang: " + strconv.FormatFloat(area, 'f', -1, 64)))
}

func calculateArea(radius int) float64 {
	area := math.Pi * math.Pow(float64(radius), 2)
	return area
}

func main() {
	http.HandleFunc("/circle-area", CircleAreaHandler)
	http.ListenAndServe(":8000", nil)
}