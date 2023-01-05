<template>
    <div>
        <form @submit.prevent="update">
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" class="form-control" name="email" v-model="form.email" />
            </div>
            <div class="form-group">
                <label for="firstname">Firstname:</label>
                <input type="text" class="form-control" name="firstname" v-model="form.firstname" />
            </div>
            <div class="form-group">
                <label for="lastname">Lastname:</label>
                <input type="text" class="form-control" name="lastname" v-model="form.lastname" />
            </div>
            <div class="form-group">
                <label for="dateOfBirth">Date of birth:</label>
                <input type="date" class="form-control" name="dateOfBirth" v-model="form.dateOfBirth" />
            </div>
            <button type="submit" class="btn btn-primary">Update</button>
        </form>
        <div v-if="message">
            {{ message }}
        </div>
    </div>
</template>

<script>

export default {
    name: 'ProfilePage',
    data() {
        return {
            form: {
                email: '',
                firstname: '',
                lastname: '',
                dateOfBirth: ''
            },
            message: '',
        };
    },
    computed: {
        currentUser() {
            return this.$store.getters.getCurrentUser;
        },
    },
    mounted() {
        if (!this.currentUser) {
            this.$router.push('/login');
        }

        this.form.email = this.currentUser.email,
        this.form.firstname = this.currentUser.firstname,
        this.form.lastname = this.currentUser.lastname,
        this.form.dateOfBirth = this.currentUser.date_of_birth
    },
    methods: {
        async update() {
            const user = {
                'email': this.form.email,
                'firstname': this.form.firstname,
                'lastname': this.form.lastname,
                'date_of_birth': this.form.dateOfBirth
            };

            try {
                await this.$store.dispatch('updateUser', [this.currentUser.id, user]);
                this.$router.push('/home');
            } catch (error) {
                this.message = error.toString();
            }
        }
    }
}
</script>
