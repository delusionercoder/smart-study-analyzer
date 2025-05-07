<template>
  <div class="add-topic-container">
    <h2>Add New Topic</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="name" class="form-label">Topic Name:</label>
        <input
          type="text"
          id="name"
          v-model="name"
          class="form-control"
          required
        />
      </div>
      <div class="form-group">
        <label for="priority" class="form-label">Priority:</label>
        <select id="priority" v-model="priority" class="form-select" required>
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
      </div>
      <div class="form-group">
        <label for="dueDate" class="form-label">Due Date:</label>
        <input
          type="date"
          id="dueDate"
          v-model="dueDate"
          class="form-control"
          required
        />
      </div>
      <div class="form-group">
        <label for="difficulty" class="form-label">Difficulty:</label>
        <input
          type="number"
          id="difficulty"
          v-model="difficulty"
          class="form-control"
          min="1"
          max="5"
          required
        />
      </div>
      <button type="submit" class="btn btn-primary">Add Topic</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'AddTopic',
  setup() {
    const name = ref('');
    const priority = ref('medium'); // Default value
    const dueDate = ref('');
    const difficulty = ref(3); // Default value

    const handleSubmit = async () => {
      const added_at = new Date(dueDate.value).toISOString();
      const newTopic = {
        name: name.value,
        added_at: added_at,
        difficulty: parseInt(difficulty.value),
        priority: priority.value,
      };

      try {
        const response = await fetch('http://127.0.0.1:8000/topics', { // Updated URL
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(newTopic),
        });

        if (response.ok) {
          console.log('Topic added successfully!');
           alert('Topic added successfully!');
          // Optionally clear the form
          name.value = '';
          priority.value = 'medium';
          dueDate.value = '';
          difficulty.value = 3;
          // Optionally redirect or show a success message
        } else {
          try {
            const errorData = await response.json(); // Attempt to get error message as JSON
            console.error('Failed to add topic:', response.status, errorData);
            alert(`Failed to add topic. Status: ${response.status}. Error: ${errorData.detail || 'No details provided.'}`);
          } catch (error) {
            console.error('Failed to parse error JSON:', error);
            alert(`Failed to add topic. Status: ${response.status}. Error: Could not parse error details.`);
          }
        }
      } catch (error) {
        console.error('Error adding topic:', error);
        alert(`Error adding topic: ${error.message}`);
        // Optionally display an error message
      }
    };

    return {
      name,
      priority,
      dueDate,
      difficulty,
      handleSubmit,
    };
  },
};
</script>

<style scoped>
.add-topic-container {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input[type="text"],
input[type="number"],
input[type="date"],
select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button[type="submit"] {
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #0056b3;
}
</style>