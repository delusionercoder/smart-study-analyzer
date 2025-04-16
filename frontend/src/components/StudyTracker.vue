<template>
  <div class="container mt-4">
    <h2>📚 Study Time Tracker</h2>

    <div class="mb-3">
      <label for="topic" class="form-label">Select Topic</label>
      <input
        type="text"
        id="topic"
        class="form-control"
        v-model="currentTopic"
        placeholder="Enter topic name"
      />
    </div>

    <div class="mb-3">
      <button class="btn btn-success me-2" @click="startTimer" :disabled="timerRunning || !currentTopic">
        Start
      </button>
      <button class="btn btn-danger" @click="stopTimer" :disabled="!timerRunning">
        Stop
      </button>
    </div>

    <p class="lead">
      Time Studied: <strong>{{ formattedTime }}</strong>
    </p>

    <hr />

    <h5>📜 Study Log</h5>
    <ul class="list-group">
      <li
        class="list-group-item"
        v-for="(log, index) in studyLog"
        :key="index"
      >
        {{ log.topic }} - {{ log.duration }} minutes
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted , computed } from 'vue'

const currentTopic = ref('')
const timerRunning = ref(false)
const startTime = ref(null)
const elapsedSeconds = ref(0)
const studyLog = ref([])

let interval = null

const startTimer = () => {
  startTime.value = Date.now()
  timerRunning.value = true

  interval = setInterval(() => {
    elapsedSeconds.value = Math.floor((Date.now() - startTime.value) / 1000)
  }, 1000)
}

const stopTimer = () => {
  timerRunning.value = false
  clearInterval(interval)

  const minutes = Math.floor(elapsedSeconds.value / 60)
  const logEntry = {
    topic: currentTopic.value,
    duration: minutes > 0 ? minutes : 1, // at least 1 minute
  }

  studyLog.value.push(logEntry)
  saveToLocalStorage()

  // reset
  elapsedSeconds.value = 0
  currentTopic.value = ''
}

const formattedTime = computed(() => {
  const mins = Math.floor(elapsedSeconds.value / 60)
  const secs = elapsedSeconds.value % 60
  return `${mins}m ${secs}s`
})

const saveToLocalStorage = () => {
  localStorage.setItem('studyLog', JSON.stringify(studyLog.value))
}

const loadFromLocalStorage = () => {
  const saved = localStorage.getItem('studyLog')
  if (saved) {
    studyLog.value = JSON.parse(saved)
  }
}

onMounted(() => {
  loadFromLocalStorage()
})
</script>
