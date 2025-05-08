<template>
  <div class="one-day-study-plan">
    <h2>One-Day Study Plan Generator</h2>
    <input v-model="subject" placeholder="Enter subject name" />
    <textarea v-model="topics" placeholder="Enter topics (comma or newline separated)"></textarea>
    <input v-model.number="hours" type="number" placeholder="Available study time (hours)" />

    <button @click="generatePlan">Generate Plan</button>

    <div v-if="studyPlan.length > 0">
      <h3>Generated Study Plan:</h3>
      <ul>
        <li v-for="(block, index) in studyPlan" :key="index">
          <strong>{{ block.time }}</strong>: {{ block.topic }}
          <button v-if="block.type === 'study'" @click="startPomodoro(block)">Start Timer</button>
        </li>
      </ul>
    </div>

    <div v-if="isPomodoroActive">
      <h3>{{ timerType === 'study' ? 'Study' : 'Break' }} Timer</h3>
      <p>{{ minutes }}:{{ seconds < 10 ? '0' + seconds : seconds }}</p>
      <button @click="stopPomodoro">Stop Timer</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const subject = ref('')
const topics = ref('')
const hours = ref(6)
const studyPlan = ref([])
const isPomodoroActive = ref(false)
const timerType = ref('')
const minutes = ref(0)
const seconds = ref(0)
let timerInterval

const generatePlan = async () => {
  studyPlan.value = []
  const response = await fetch('http://localhost:8000/generate-one-day-plan', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      subject: subject.value,
      topics: topics.value,
      hours: hours.value,
    }),
  })

  if (response.ok) {
    const data = await response.json()
    studyPlan.value = data.plan
  } else {
    console.error('Failed to generate study plan')
  }
}

const startPomodoro = (block) => {
  // Set the timer duration based on study or break
  if (block.type === 'study') {
    minutes.value = 25
    timerType.value = 'study'
  } else {
    minutes.value = 5
    timerType.value = 'break'
  }

  isPomodoroActive.value = true
  timerInterval = setInterval(updateTimer, 1000)
}

const updateTimer = () => {
  if (seconds.value === 0) {
    if (minutes.value === 0) {
      clearInterval(timerInterval)
      isPomodoroActive.value = false
      alert(`${timerType.value === 'study' ? 'Study' : 'Break'} time over!`)
    } else {
      minutes.value -= 1
      seconds.value = 59
    }
  } else {
    seconds.value -= 1
  }
}

const stopPomodoro = () => {
  clearInterval(timerInterval)
  isPomodoroActive.value = false
}
</script>

<style scoped>
.one-day-study-plan {
  padding: 20px;
}

button {
  margin-top: 10px;
}
</style>
