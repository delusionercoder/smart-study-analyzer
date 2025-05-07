<template>
  <div class="show-topics-container">
    <h2>All Topics</h2>
    <div v-if="loading">Loading topics...</div>
    <div v-else-if="error">Error loading topics: {{ error }}</div>
    <table v-else-if="topics.length > 0">
      <thead>
        <tr>
          <th>Name</th>
          <th>Added At</th>
          <th>Difficulty</th>
          <th>Priority</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="topic in topics" :key="topic._id">
          <td>{{ topic.name }}</td>
          <td>{{ formatDate(topic.added_at) }}</td>
          <td>{{ topic.difficulty }}</td>
          <td>{{ topic.priority }}</td>
        </tr>
      </tbody>
    </table>
    <div v-else>No topics added yet.</div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
  name: 'ShowTopics',
  setup() {
    const topics = ref([]);
    const loading = ref(true);
    const error = ref(null);

    const fetchTopics = async () => {
      try {
        const response = await fetch('http://localhost:8000/topics'); // Ensure correct backend URL
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        topics.value = data;
      } catch (err) {
        error.value = err.message;
      } finally {
        loading.value = false;
      }
    };

    const formatDate = (dateTimeString) => {
      if (!dateTimeString) {
        return '-';
      }
      try {
        const date = new Date(dateTimeString);
        return date.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' });
      } catch (e) {
        console.error('Error formatting date:', e);
        return dateTimeString; // Fallback to the original string
      }
    };

    onMounted(fetchTopics);

    return {
      topics,
      loading,
      error,
      formatDate,
    };
  },
};
</script>

<style scoped>
.show-topics-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th,
td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

.loading {
  text-align: center;
  font-style: italic;
  color: #777;
}

.error {
  color: red;
  text-align: center;
  margin-top: 10px;
}

.empty {
  text-align: center;
  color: #777;
}
</style>