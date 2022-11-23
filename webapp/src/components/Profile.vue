<template>
    <div>
        <form @submit.prevent="update">
            <div>
                <label for="email">Email:</label>
                <input type="email" name="email" v-model="form.email" />
            </div>
            <div>
                <label for="firstname">Firstname:</label>
                <input type="text" name="firstname" v-model="form.firstname" />
            </div>
            <div>
                <label for="surname">Surname:</label>
                <input type="text" name="surname" v-model="form.surname" />
            </div>
            <div>
                <label for="dateOfBirth">Date of birth:</label>
                <input type="date" name="dateOfBirth" v-model="form.dateOfBirth" />
            </div>
            <button type="submit">Update</button>
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
                surname: '',
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
        this.form.surname = this.currentUser.surname,
        this.form.dateOfBirth = this.currentUser.date_of_birth
    },
    methods: {
        async update() {
            const user = {
                'email': this.form.email,
                'firstname': this.form.firstname,
                'surname': this.form.surname,
                'date_of_birth': this.form.dateOfBirth
            };

            console.log(user)

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
