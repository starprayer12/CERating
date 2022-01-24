import { ref, reactive } from "vue";

export const loginForm = reactive({
    account: "",
    password: "",
});

export const rulesLogin = ref({
    account: [
        {
            required: true,
            message: "Account could not be empty!",
            trigger: "blur",
        },
    ],
    password: [
        {
            required: true,
            message: "Password could not be empty!",
            trigger: "blur",
        },
        {
            min: 6,
            max: 30,
            message: "Password's length has to be 6 to 30 characters!",
            trigger: "blur",
        },
    ],
});