import React, {useCallback, useEffect, useState} from 'react';
import CompletionRateChart from './GoalsCharts/ComplationRateChart.js';
import HappinessChart from "./GoalsCharts/HappinessChart.js";
import ChartSkeleton from "./GoalsCharts/ChartSkeleton";
import AccomplishmentsChart from "./GoalsCharts/AccomplishmentsChart.js";
import PlansChart from "./GoalsCharts/PlansChart.js";
import ReportedProblemsChart from "./GoalsCharts/ReportedProblemsChart.js";
import {Col} from "antd";
import {weeklyStatus} from "@models/weeklyStatus";
import {goalSkeleton} from "./GoalSkeletons";
import {chartsData, dateIntervalDataWS, goalsStatusWSData} from "@store";
import {useRecoilState, useRecoilValue} from "recoil";
import {CSSTransition, SwitchTransition} from "react-transition-group";
import {getProgressBarSections, goalsStatusPercentageList} from "../WSDashboard.config";

const GoalsStatusAndCharts = () => {
    const [goalsWSData, setGoalsWSData] = useRecoilState(goalsStatusWSData);
    const [goalStatuses, SetGoalStatuses] = useState({});
    const [isGoalsDataLoading, SetGoalsDataLoadStatus] = useState(true);
    const dateIntervalData = useRecoilValue(dateIntervalDataWS);
    const [isLoading, SetLoading] = useState(true);
    const [allChartsData, setAllChartsData] = useRecoilState(chartsData);
    const [happinessData, SetHappinessData] = useState(null);
    const [CRData, SetCRData] = useState(null);
    const [accomplishmentsData, SetAccomplishmentsData] = useState(null);
    const [planData, SetPlanData] = useState(null);
    const [challengeData, SetChallengeData] = useState(null);

    useEffect(() => {
        const startDate = dateIntervalData?.start ? dateIntervalData.start : "";
        const endDate = dateIntervalData?.end ? dateIntervalData.end : "";

        weeklyStatus.getGoalsData(startDate, endDate).then(res => {
            if (res?.data?.status) {
                setGoalsWSData(res.data);
                SetGoalsDataLoadStatus(false);
            }
        })
    }, [dateIntervalData, setGoalsWSData]);

    useEffect(() => {
        if (!!Object.keys(goalsWSData).length) {
            let statusObj = {};
            const {
                goals_statuses_count: {
                    on_track: {count: countOnTrack},
                    at_risk: {count: countAtRisk},
                    off_track: {count: countOffTrack},
                    exceeded: {count: countExceeded},
                    completed: {count: countCompleted}
                }
            } = goalsWSData;
            statusObj.onTrack = countOnTrack;
            statusObj.atRisk = countAtRisk;
            statusObj.offTrack = countOffTrack;
            statusObj.exceeded = countExceeded;
            statusObj.completed = countCompleted;
            statusObj.progressed = goalsWSData.progressed;
            SetGoalStatuses(statusObj);
        }
    }, [goalsWSData]);

    const getPercentage = useCallback((sect) => {
        let arrayOfValues = Object.values(goalStatuses);
        if (!!arrayOfValues.length) {
            // get the percentage and then trunc the result to the first floating point number
            if (sect === 'onTrack') {
                return !!goalsWSData.goals_total_count ? Math.trunc(((arrayOfValues[0] * 100) / goalsWSData.goals_total_count) * 10) / 10: goalsWSData.goals_total_count;
            } else if (sect === 'atRisk') {
                return !!goalsWSData.goals_total_count ? Math.trunc(((arrayOfValues[1] * 100) / goalsWSData.goals_total_count) * 10) / 10 : goalsWSData.goals_total_count;
            } else if (sect === 'offTrack') {
                return !!goalsWSData.goals_total_count ? Math.trunc(((arrayOfValues[2] * 100) / goalsWSData.goals_total_count) * 10) / 10 : goalsWSData.goals_total_count;
            } else if (sect === 'exceeded') {
                return !!goalsWSData.goals_total_count ? Math.trunc(((arrayOfValues[3] * 100) / goalsWSData.goals_total_count) * 10) / 10 : goalsWSData.goals_total_count;
            } else if (sect === 'completed') {
                return !!goalsWSData.goals_total_count ? Math.trunc(((arrayOfValues[4] * 100) / goalsWSData.goals_total_count) * 10) / 10 : goalsWSData.goals_total_count;
            } else {
                return arrayOfValues[5];
            }
        }
    }, [goalStatuses, goalsWSData.goals_total_count]);

    useEffect(() => {
        const startDate = dateIntervalData?.start ? dateIntervalData.start : "";
        const endDate = dateIntervalData?.end ? dateIntervalData.end : "";
        weeklyStatus.getChartsData(startDate, endDate).then(res => {
            if (res?.data?.success) {
                setAllChartsData(res.data);
            }
        })
    }, [setAllChartsData, dateIntervalData]);

    useEffect(() => {
        if (!!Object.keys(allChartsData).length) {
            let [completionRate, accomplishment, plan, challenge, satisfaction] = [{}, {}, {}, {}, {}];
            completionRate.percent = allChartsData.completion_percent;
            completionRate.data = allChartsData.completion_rate;
            accomplishment.sum = allChartsData.accomplishments_sum;
            accomplishment.data = allChartsData.accomplishments;
            accomplishment.users = allChartsData.accomplishmentsUsers.count;
            plan.sum = allChartsData.plans_sum;
            plan.data = allChartsData.plans;
            plan.users = allChartsData.plansUsers.count;
            satisfaction.data = allChartsData.happiness;
            challenge.sum = allChartsData.challenges_sum;
            challenge.data = allChartsData.challenges;
            challenge.users = allChartsData.challengesUsers.count;
            completionRate.accomplishmentsSum = allChartsData.accomplishments_sum
            completionRate.plansSum = allChartsData.plans_sum;
            SetAccomplishmentsData(accomplishment);
            SetPlanData(plan);
            satisfaction.avg = allChartsData.happiness_avg;
            SetHappinessData(satisfaction);
            SetChallengeData(challenge);
            SetCRData(completionRate);
            SetLoading(false);
        }
    }, [allChartsData]);

    const chartsDataArr = useCallback(() => {
        return [
            {
                data: CRData,
                get component() {
                    return <CompletionRateChart data={this.data}/>
                }
            },
            {
                data: happinessData,
                get component() {
                    return <HappinessChart data={this.data}/>
                }
            },
            {
                data: accomplishmentsData,
                get component() {
                    return <AccomplishmentsChart data={this.data}/>
                }
            },
            {
                data: planData,
                get component() {
                    return <PlansChart data={this.data}/>
                }
            },
            {
                data: challengeData,
                get component() {
                    return <ReportedProblemsChart data={this.data}/>
                }
            }
        ]
    }, [
        CRData,
        accomplishmentsData,
        planData,
        challengeData,
        happinessData
    ]);

    return (
        <>
            <Col span={24} className="goals_status">
                <div>
                    <p className="secondary_title">Goals Status</p>
                    <span>for the week</span>
                </div>
                <ul className="goal_status_list">
                    <SwitchTransition>
                        <CSSTransition
                            key={isGoalsDataLoading ? "1" : "2"}
                            classNames='animation'
                            timeout={300}
                            unmountOnExit={true}
                        >
                            {isGoalsDataLoading ? <>{goalSkeleton(goalsStatusPercentageList(getPercentage).length)}</> : <>{
                                goalsStatusPercentageList(getPercentage).map((item, index) => {
                                    return (
                                        <li className={item.rightBorder ? 'goal_status_item right_bordered' : item.className}
                                            key={item.title + index}
                                        >
                                    <span>
                                        {item.value}
                                        <div className={item.colorIndicator ? 'color-indicator' : 'indicator-none'}/>
                                    </span>
                                            <span>{item.title}</span>
                                        </li>
                                    )
                                })
                            }</>}
                        </CSSTransition>
                    </SwitchTransition>
                </ul>
            </Col>
            <Col span={24}>
                <div className="goals_progress_bar">
                    {getProgressBarSections.map(item => <div
                        key={item.percentageArg}
                        className={item.className}
                        style={{width: `${getPercentage(item.percentageArg)}%`}}
                    />)}
                </div>
            </Col>
            <Col span={24} className="charts_container">
                <section className="goals_charts_section">
                    {
                        chartsDataArr().map((item, index) => <SwitchTransition key={index}>
                            <CSSTransition
                                key={!isLoading && item.data.length ? "1" : "2"}
                                classNames='animation'
                                timeout={300}
                                unmountOnExit={true}
                            >
                                {!isLoading ? item.component : <ChartSkeleton/>}
                            </CSSTransition>
                        </SwitchTransition>)
                    }
                </section>
            </Col>
        </>
    );
}

export default React.memo(GoalsStatusAndCharts);